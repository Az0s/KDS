/*
 * @Date: 2022-03-25 19:03:59
 * @LastEditors: Azus
 * @LastEditTime: 2022-03-27 19:23:28
 * @FilePath: /KDS/frontend/src/components/Classifier.js
 */
import React, {useRef, useEffect, useState} from 'react';
import Predictions from './Predictions';
import Grid from '@material-ui/core/Grid';
import { makeStyles } from '@material-ui/core/styles';
import {InfoSnackbar, LoadingSnackbar } from './Snackbars'
import DropImageCard from './DropImageCard'
import { fetchImage, makeSession, loadModel, runModel } from './utils'
// import Button from '@material-ui/core/Button';

const session = makeSession();

const useStyles = makeStyles(theme => ({
    root: {
      flexGrow: 1,
    },
  }));
  

export default function Classifier() {
    const [loaded, setLoaded] = useState(false);
    const [isLoading, setIsLoading] = useState(false);
    
    //v1
    // const startLoadModel = async () => {
    //     if (isLoading || loaded) { return; }
    //     setIsLoading(true);
    //     await loadModel(session);
    //     setLoaded(true);
    //     setIsLoading(false);
    // }
    
    const [file, setFile] = useState(null)    
    const canvas = useRef(null)
    const [data, setData] = useState(null)
    
    // V2   
    useEffect(() => {
        if (file)   runModel(session, file, setOutput);
    }, [file])

    // V1
    useEffect(() => {
        if (file) fetchImage(file, canvas, setData);
    }, [file])

    // const [outputMap, setOutputMap] = useState(null);
    
    const [output, setOutput] = useState(null)
    useEffect(() => {
        if (!loaded || !data) return;
        runModel(session, data, setOutput);
    }, [loaded, data]); // runs when loaded or data changes    
    
    // const outputData = outputMap && outputMap.values().next().value.data;
    
    const classes = useStyles();

    return <div className={classes.root}>
        <Grid container spacing={3}>
            
            {/* <Grid item>
                <DropImageCard setFile={setFile} canvasRef={canvas} fileLoaded={!!file} />
                { !loaded && !isLoading && <Button variant="contained" onClick={startLoadModel}>Load Classifier</Button>}
                { !loaded && isLoading && <LoadingSnackbar message="Loading model..." /> }
                { loaded && data && !outputMap && <LoadingSnackbar message="Running model..." /> }
                { loaded && !file && <InfoSnackbar message="Add or take a picture..." /> }
                { !!file && !data && <LoadingSnackbar message="Loading image..." /> }
            </Grid>
             */}

            {/* V2 */}

                        
            <Grid item>
                <DropImageCard setFile={setFile} canvasRef={canvas} fileLoaded={!!file} />
                
                {/* { data && !output && <LoadingSnackbar message="Running model..." /> } */}
                { !file && <InfoSnackbar message="Add or take a picture..." /> }
                { !!file && !output && <LoadingSnackbar message="Running model..." /> } 
            </Grid>

            <Grid item>
                <Predictions output={output} />
            </Grid>
        </Grid>
    </div>
}