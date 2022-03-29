/*
 * @Date: 2022-03-26 21:44:59
 * @LastEditors: Azus
 * @LastEditTime: 2022-03-29 15:46:25
 * @FilePath: /KDS/frontend/src/components/Predictions.js
 */
import React from 'react';
import Scorecard from './Scorecard';

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
    return <Scorecard items={item} />;
}