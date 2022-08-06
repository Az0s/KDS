/*
 * @Date: 2022-04-14 22:32:58
 * @LastEditors: Azus
 * @LastEditTime: 2022-04-18 13:42:47
 * @FilePath: /KDS/frontend/src/components/Popover.js
 */
import clsx from "clsx";
import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Popover from "@material-ui/core/Popover";
import Typography from "@material-ui/core/Typography";
import Button from "@material-ui/core/Button";
import HelpIcon from "@material-ui/icons/Help";
import { Box } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  typography: {
    padding: theme.spacing(2),
  },
  box: {
    width: 299,
    padding: 0,
    margin: 0,
  },
  content: {
    boxSizing: "border-box",
  },
  info: {
    backgroundColor: theme.palette.primary.main,
  },
  icon: {
    fontSize: 20,
  },
  iconVariant: {
    opacity: 0.9,
    marginRight: theme.spacing(1),
  },
  message: {
    display: "flex",
    alignItems: "center",
  },
}));

export default function SimplePopover({contents}) {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = React.useState(null);

  const handleClick = (event) => {
    setAnchorEl(event.currentTarget);
  };

  const handleClose = () => {
    setAnchorEl(null);
  };

  const open = Boolean(anchorEl);
  const id = open ? "simple-popover" : undefined;

  return (
    <div>
      <Button
        fullWidth
        aria-describedby={id}
        variant="contained"
        color="primary"
        onClick={handleClick}
      >
        <HelpIcon
          className={clsx(classes.icon, classes.iconVariant)}
        ></HelpIcon>
        Treatment
      </Button>
      <Popover
        id={id}
        open={open}
        anchorEl={anchorEl}
        onClose={handleClose}
        anchorOrigin={{
          vertical: "bottom",
          horizontal: "center",
        }}
        transformOrigin={{
          vertical: "top",
          horizontal: "center",
        }}
      >
        <Typography className={classes.typography} variant="h5">
          Infectious keratitis
        </Typography>
        <Typography className={classes.typography} variant="body1">
          Treatment of infectious keratitis varies, depending on the cause of
          the infection.
        </Typography>

        <Typography className={classes.typography}>
          <strong> Bacterial keratitis. </strong>
          For mild bacterial keratitis, antibacterial eyedrops may be all you
          need to effectively treat the infection. If the infection is moderate
          to severe, you may need to take oral antibiotics to get rid of the
          infection.
        </Typography>
        <Typography className={classes.typography}>
          <strong> Fungal keratitis. </strong>
          Fungal keratitis. Keratitis caused by fungi typically requires
          antifungal eyedrops and oral antifungal medication.
        </Typography>
        <Typography className={classes.typography}>
          <strong> Viral keratitis. </strong>
          Viral keratitis. If a virus is causing the infection, antiviral
          eyedrops and oral antiviral medications may be effective. Other
          viruses need only supportive care such as artificial tear drops.
        </Typography>
        <Typography className={classes.typography}>
          <strong> Acanthamoeba keratitis. </strong>
          Acanthamoeba keratitis. Keratitis that's caused by the tiny parasite
          acanthamoeba can be difficult to treat. Antibiotic eyedrops are used,
          but some acanthamoeba infections are resistant to medication. Severe
          cases of acanthamoeba keratitis may require a cornea transplant.
        </Typography>
        <Typography className={classes.typography}>{contents}</Typography>
        <Typography className={classes.typography}>{contents}</Typography>
      </Popover>
    </div>
  );
}
