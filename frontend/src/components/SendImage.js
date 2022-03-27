/*
 * @Date: 2022-03-25 20:30:53
 * @LastEditors: Azus
 * @LastEditTime: 2022-03-26 16:13:34
 * @FilePath: /react-ml-app/frontend/src/components/SendImage.js
 */
// /*
//  * @Date: 2022-03-25 20:30:53
//  * @LastEditors: Azus
//  * @LastEditTime: 2022-03-25 20:37:32
//  * @FilePath: /react-ml-app/src/components/sendImage.js
//  */
// import React, { useState } from "react";
// import Button from "@material-ui/core/Button";

// const SendImage = () => {
//   const [image, setImage] = useState();

//   const handleSubmit = (e) => {
//     e.preventDefault();
//     let fileToUpload = image;
//     const formData = new FormData();
//     formData.append("file", fileToUpload);

//     fetch("/api/upload", {
//       method: "POST",
//       headers: {
//         "Content-Type": "multipart/form-data",
//         Accept: "multipart/form-data",
//       },
//       body: formData,
//     }).then((resp) => {
//       resp.json().then((data) => {
//         console.log(data);
//       });
//     });
//   };

//   return (
//     <form
//       onSubmit={handleSubmit}
//       className="container mt-5 pt-5 pb-5"
//       encType="multipart/form-data"
//     >
//       <div className="form-inline justify-content-center mt-5">
//         <label htmlFor="image" className="ml-sm-4 font-weight-bold mr-md-4">
//           Image :{" "}
//         </label>
//         <div className="input-group">
//           <input
//             onChange={(e) => {
//               setImage(e.target.files[0]);
//             }}
//             type="file"
//             id="image"
//             name="file"
//             accept="image/*"
//             className="file-custom"
//           />
//         </div>
//       </div>

//       <div className="input-group justify-content-center mt-4">
//         <Button
//           variant="contained"
//           type="submit"
//           className="btn btn-md btn-primary"
//         >
//           Upload...
//         </Button>
//       </div>
//     </form>
//   );
// };

// export default SendImage;

import React from 'react'
// import Button from "@material-ui/core/Button";
import Input from "@material-ui/core/Input";

const SendImage = () => {
  return (
    <>
      <form method="POST" action="/api/upload">
          <Input required type="file" size="30" name="photo" />
          <Input  type="submit" size="30" name="photo" />
      </form>
    </>
  );
}

export default SendImage

