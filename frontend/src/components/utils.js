import loadImage from "blueimp-load-image";
import { InferenceSession } from "onnxjs";
import axios from "axios";

export const makeSession = (() => {
  let _session = null;
  return () => {
    if (_session !== null) {
      return _session;
    }
    return new InferenceSession({ backendHint: "webgl" });
  };
})();


async function _runModel(predict_url, session, file, setOutput) {
  // const {width, height} = input;
  console.log(file);
  const fd = new FormData();
  fd.append("image", file);
  console.log(fd);
  axios.post(predict_url, fd).then((res) => {
    console.log(res.data);
    setOutput(res.data);
  });
  // const data = preprocess(input);
  // const inputTensor = new Tensor(data, 'float32', [1, 3, width, height]);
  // await wait(0);
  // const outputMap = await session.run([inputTensor]);
}

export function runModel(predict_url, session, file, setOutput) {
  setTimeout(() => _runModel(predict_url, session, file, setOutput), 10);
}

const wait = (ms) =>
  new Promise((res, rej) => {
    global.setTimeout(() => res(), ms);
  });

const imgConfig = {
  maxWidth: 299,
  maxHeight: 299,
  cover: true,
  crop: true,
  canvas: true,
  crossOrigin: "Anonymous",
  orientation: true,
};

const getImage = (url) =>
  new Promise((res, rej) => {
    loadImage(url, (img) => res(img), imgConfig);
  });

export const fetchImage = async (url, canvas, setData) => {
  if (!canvas || !canvas.current) return;
  const img = await getImage(url);
  if (img.type === "error") throw new Error("could not load image");
  const ctx = canvas.current.getContext("2d");
  ctx.drawImage(img, 0, 0);
  await wait(1);
  const data = ctx.getImageData(
    0,
    0,
    canvas.current.width,
    canvas.current.height
  );
  setData(data);
};
