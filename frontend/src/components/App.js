/*
 * @Date: 2022-03-25 19:03:59
 * @LastEditors: Azus
 * @LastEditTime: 2022-04-14 11:45:08
 * @FilePath: /KDS/frontend/src/components/App.js
 */
import React from 'react';
import Classifier from './Classifier'
import Container from '@material-ui/core/Container';
import Typography from '@material-ui/core/Typography';

import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Expansion from './Expansion'
import Button from '@material-ui/core/Button';
// import SendImage from "./SendImage";

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
    },
    content: {
        marginTop: 20,
    },
    menuButton: {
        marginRight: theme.spacing(2),
    },
    title: {
        flexGrow: 1,
    },
    heading: {
        fontSize: theme.typography.pxToRem(15),
        fontWeight: theme.typography.fontWeightRegular,
    },
    table: {
        width: '100%',
    },
    footer: {
        padding: theme.spacing(2),
        marginTop: 'auto',
    },
    button: {
        margin: theme.spacing(1),
    },
}));

function App() {
    const classes = useStyles();
    return (
      <div className={classes.root}>
        {/* App Bar  */}
        <AppBar position="static">
          <Toolbar>
            <img
              src="https://s1.ax1x.com/2022/04/14/Ll9ERS.png"
              height="50px"
              align="center"
            />
            <Typography variant="h6" className={classes.title}>
              Keratitis Diagnosis System
            </Typography>
          </Toolbar>
        </AppBar>

        <Container className={classes.content}>
          <Classifier />
          {/* <SendImage /> */}
        </Container>
        <Container className={classes.content}>
          {/* Foot Expansion */}
          <Expansion classes={classes} />

          {/* Footer */}
          <footer className={classes.footer}>
            <Button className={classes.button}>Privacy Policy</Button>
            <Button className={classes.button}>KDS - BUPT 2022</Button>
            <Button className={classes.button}>CONTACT</Button>
          </footer>
        </Container>
      </div>
    );
}

export default App;
