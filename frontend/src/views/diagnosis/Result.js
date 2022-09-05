import { CChartDoughnut } from '@coreui/react-chartjs'
import { CCard, CCardHeader, CCardImage, CCardText, CCardBody, CCardTitle } from '@coreui/react'
import React, { useState } from 'react'
import { useSelector } from 'react-redux'
const Result = (res) => {
  // debugger
  const [img, setImg] = useState(undefined)
  const form = useSelector((state) => state.form)
  console.log(form)
  let reader = new FileReader()
  reader.readAsDataURL(form.image[0])
  reader.onload = (e) => {
    setImg(e.target.result)
    // console.log(e.target.result)
  }

  var data = {
    labels: [],
    datasets: [
      {
        data: [],
        backgroundColor: ['#FF6‰84', '#4BC0C0', '#FFCE56', '#36A2EB'],
      },
    ],
  }
  Object.keys(res.result).forEach((key) => {
    data.labels.push(key)
    data.datasets[0].data.push(res.result[key])
  })
  // debugger
  const type = data.labels[data.datasets[0].data.indexOf(Math.max(...data.datasets[0].data))]
  return (
    <div>
      <CCard>
        <CCardHeader>
          <strong> Results </strong>
        </CCardHeader>
        <CCardBody>
          <CCardTitle>Congrats!</CCardTitle>
          <p className="text-medium-emphasis small">Your image is successfully identified!</p>

          {/* <strong>Uploaded image</strong>
          <hr /> */}
          <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'space-around' }}>
            <CCard
              style={{ margin: '30px', width: '300px', display: 'inline-flex', border: '0px' }}
            >
              <CCardImage
                style={{
                  borderTopLeftRadius: '3px',
                  borderTopRightRadius: '3px',
                  borderBottomLeftRadius: '3px',
                  borderBottomRightRadius: '3px',
                }}
                orientation="bottom"
                src={img}
              />
              <CCardBody style={{ backgroundcolor: 'grey' }}>
                <CCardTitle align="left">{form.name}</CCardTitle>
                <CCardText>
                  <font align="left">Type:</font>
                  <font color="36A2EB">
                    <strong align="right">{type}</strong>
                  </font>
                  <br />

                  <font align="left">Private:</font>
                  <strong>{form.shareSwitch ? 'No' : 'Yes'}</strong>
                </CCardText>
              </CCardBody>
            </CCard>
            {/* <strong>Result</strong>
            <hr /> */}
            <CChartDoughnut style={{ display: 'inline-flex', width: '300px' }} data={data} />
          </div>
        </CCardBody>
      </CCard>
    </div>
  )
}

export default Result
