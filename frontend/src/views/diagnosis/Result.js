import { CChartDoughnut } from '@coreui/react-chartjs'
import {
  CCard,
  CCardHeader,
  CCardImage,
  CCardText,
  CCardBody,
  CCol,
  CRow,
  CCardTitle,
} from '@coreui/react'
import React, { useState } from 'react'
import { useSelector } from 'react-redux'
const Result = (res) => {
  // debugger
  const [img, setImg] = useState()
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
          <CRow>
            <CCol center md={4} sm={6} xs={10}>
              <strong>Uploaded image</strong>
              <hr />
              <CCard align="center" style={{ margin: '10px' }}>
                <CCardImage orientation="bottom" src={img} width="10wh" />
                <CCardBody>
                  <CCardTitle align="left">{form.name}</CCardTitle>
                  <CCardText>
                    <CRow>
                      <CCol align="left">type:</CCol>
                      <CCol>
                        <font color="36A2EB">
                          <strong>{type}</strong>
                        </font>
                      </CCol>
                    </CRow>
                    <CRow>
                      <CCol align="left">Private:</CCol>
                      <CCol>
                        <strong>{form.shareSwitch ? 'No' : 'Yes'}</strong>
                      </CCol>
                    </CRow>
                  </CCardText>
                </CCardBody>
              </CCard>
            </CCol>
            <CCol>
              <div>
                <strong>Result</strong>
                <hr />
                <CChartDoughnut style={{ width: '18rem' }} data={data} />
              </div>
            </CCol>
          </CRow>
        </CCardBody>
      </CCard>
    </div>
  )
}

export default Result
