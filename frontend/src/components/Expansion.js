/*
 * @Date: 2022-03-25 19:24:20
 * @LastEditors: Azus
 * @LastEditTime: 2022-03-27 23:53:22
 * @FilePath: /KDS/frontend/src/components/Expansion.js
 */
import React from 'react'
import ExpansionPanel from '@material-ui/core/ExpansionPanel';
import ExpansionPanelSummary from '@material-ui/core/ExpansionPanelSummary';
import ExpansionPanelDetails from '@material-ui/core/ExpansionPanelDetails';
import ExpandMoreIcon from '@material-ui/icons/ExpandMore';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Avatar from '@material-ui/core/Avatar';
// import credits from './credits';
import Link from '@material-ui/core/Link';

import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";


const Expansion = ({classes}) => {
  return (
    <>
      <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography className={classes.heading}>
            How do I use this?
          </Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography variant="body2">
            Tab on the image icon to take a photo of a patient's eye or drag and
            drop an image file on the image icon to diagnosis. <br />
            <br />
            Note that only 4 kinds of keratits are currently supported. If your
            image shows a different type, the prediction will be inaccurate.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel1a-content"
          id="panel1a-header"
        >
          <Typography className={classes.heading}>
            How did we achieve this?
          </Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography variant="body2">
            <img
              src="https://s2.loli.net/2022/03/27/JMk8XdQKRDThvow.png"
              width="90%"
            />
            <br />
            <span>
              <b>Model enhancement </b>
              <br />
              <br />
              ·Histogram Equalization <br />
              ·Image Normalization <br />
              ·Image Transform <br />
              ·Using Pre-trained Model <br />
              ·Learning Rate Adjustment <br />
              <br />
              Using model blending technique to fuse weak classfiers into strong
              classfiers <br /> The final combination is
              <b> ResNext101_32x8d + DenseNet121</b> whose average accuracy on
              our database can reach 76.70%
              <br />
              <br />
            </span>
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel2a-content"
          id="panel2a-header"
        >
          <Typography className={classes.heading}>
            What types of keratits does the classifier supports?
          </Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography variant="body2">
            This classifier is based on the{" "}
            <Link to="http://vision.stanford.edu/aditya86/ImageNetDogs/">
              Keratits Dataset
            </Link>{" "}
            and currently supports 4 types of keratits: amb micro fubgus and
            virus.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      {/* <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel3a-content"
          id="panel3a-header"
        >
          <Typography className={classes.heading}>
            What is this good for?
          </Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography variant="body2">This app is not</Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel> */}
      <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel3a-content"
          id="panel3a-header"
        >
          <Typography className={classes.heading}>
            What happens to my data?
          </Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Typography variant="body2">
            No image that you take with or add to this application will be
            stored on our or anyone's servers by this application / website and
            is encrypted-delivered.
          </Typography>
        </ExpansionPanelDetails>
      </ExpansionPanel>
      <ExpansionPanel>
        <ExpansionPanelSummary
          expandIcon={<ExpandMoreIcon />}
          aria-controls="panel3a-content"
          id="panel3a-header"
        >
          <Typography className={classes.heading}>Credits</Typography>
        </ExpansionPanelSummary>
        <ExpansionPanelDetails>
          <Container>
            <Typography variant="body2">
              The Dataset is from{" "}
              <a href="https://www.trhos.com/">
                BeiJing TONGRENG Hospital, CMU{" "}
              </a>
              and its patients.
              <br />
              Thanks to Mentors:
              <Table className={classes.table}>
                <TableHead>
                  <TableRow>
                    <TableCell>Mentors Name</TableCell>
                    <TableCell>Organization</TableCell>
                    <TableCell>Specialize</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>欧中洪</TableCell>
                    <TableCell>BUPT, SCS</TableCell>
                    <TableCell>DL, Big Data</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>胡春</TableCell>
                    <TableCell>BUPT, SEM</TableCell>
                    <TableCell>Marketing Management</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>杜振华</TableCell>
                    <TableCell>BUPT, SEM</TableCell>
                    <TableCell>Applied Economy, Industry Economy</TableCell>
                  </TableRow>
                  <TableRow>
                    <TableCell>刘武</TableCell>
                    <TableCell>TRHOS</TableCell>
                    <TableCell>
                      Chief Physician, Centre for Ophthalmology
                    </TableCell>
                  </TableRow>
                </TableHead>
              </Table>
              <br/>
              <i>dev: 李旭宸，郭子义</i>
            </Typography>
          </Container>
        </ExpansionPanelDetails>
      </ExpansionPanel>
    </>
  );
}

export default Expansion