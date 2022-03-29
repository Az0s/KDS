/*
 * @Date: 2022-03-26 21:44:59
 * @LastEditors: Azus
 * @LastEditTime: 2022-03-27 19:23:08
 * @FilePath: /KDS/frontend/src/components/Predictions.js
 */
import React from 'react';
import classes from './classes'
import Scorecard from './Scorecard';
// import {getBreedImg, getBreed} from './utils';

// const getTopK = (acts, k) => {
//     const topK = Array.from(acts)
//         .map((act, i) => [act, i])
//         .sort((a, b) => {
//             if (a[0] < b[0]) return -1;
//             if (a[0] > b[0]) return 1;
//             return 0;
//         })
//         .reverse()
//         .slice(0, k)

//     // denominator of softmax function
//     const denominator = acts.map(y => Math.exp(y)).reduce((a,b) => a+b)
//     return topK.map(([act, i], _, acts) => ({
//         breed: classes[i],
//         act,
//         prob: Math.exp(act) / denominator,
//     }));
// }

// export default function Predictions({output}) {
//     if (!output) return null;
//     const items = getTopK(output, 5).map(({breed, prob}) => ({
//         name: getBreed(breed),
//         percentage: (prob * 100).toFixed(2),
//         avatar: getBreedImg(breed),
//     }));

//     return <Scorecard items={items} />;
// }
export default function Predictions({output}) {
    const ImgUrlOfType = {
      amb: "https://cdn1.iconfinder.com/data/icons/virus-3/512/virus-bacteria-microorganism-02-1024.png",
      fungus:
        "https://cdn1.iconfinder.com/data/icons/farming-agriculture-3/42/fungi-1024.png",
      micro:
        "https://cdn2.iconfinder.com/data/icons/coronavirus-9/512/virus-cell-life-biology-Microorganism-1024.png",
      virus:
        "https://cdn4.iconfinder.com/data/icons/covid-19-62/512/covid-coronavirus-20-1024.png",
    };
    if (!output) return null;
    const item = Object.keys(output).map((key)=>( {
        avatar:ImgUrlOfType[key],
        name:key, 
        percentage:output[key],
    }))
    console.log(item)
    // const items = output.map(({type, prob}) => ({
    //     name: {type},
    //     percentage: {prob},
    //     // avatar: getBreedImg(breed),
    // }));
    // console.log(output)

    return <Scorecard items={item} />;
}