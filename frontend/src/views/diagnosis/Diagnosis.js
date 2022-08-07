import React from 'react'
import {
  CButton,
  CCard,
  CCardBody,
  CCardHeader,
  CCol,
  CForm,
  CFormInput,
  CFormLabel,
  CInputGroup,
  CFormSwitch,
  CFormSelect,
  CFormFeedback,
  CRow,
} from '@coreui/react'
import { useForm } from 'react-hook-form'
import axios from 'axios'
const FormControl = () => {
  const { register, handleSubmit } = useForm()
  const onSubmit = (data) => {
    console.log(data)
    axios
      .post('http://101.43.232.154:8080/predict', data, {
        headers: { 'Access-Control-Allow-Origin': '*' },
      })
      .then((res) => {
        console.log(res.data)
      })
  }

  return (
    <CRow>
      <CCol xs={12}>
        <CCard className="mb-4">
          <CCardHeader>
            <strong>Start Diagnosis</strong> <small>Upload photo to start diagnosis</small>
          </CCardHeader>
          <CCardBody>
            <CForm onSubmit={handleSubmit(onSubmit)}>
              {/* <DocsExample href="forms/form-control#file-input"> */}

              <CCol className="mb-3" md={6}>
                <CFormLabel htmlFor="formName">SOME TEXT</CFormLabel>
                <CInputGroup className="has-validation">
                  <CFormInput
                    {...register('name')}
                    type="text"
                    id="formName"
                    placeholder="Input Name"
                    required
                  />
                  <CFormFeedback invalid>Please choose a username.</CFormFeedback>
                </CInputGroup>
              </CCol>
              <CCol className="mb-3" md={3}>
                <CFormLabel htmlFor="formType" required>
                  Select image type:
                </CFormLabel>
                <CFormSelect {...register('type')} aria-label="Select type:" id="formType">
                  <option>Select type</option>
                  <option value="jpeg">jpeg</option>
                  <option value="png">png</option>
                  <option value="tiff">tiff</option>
                </CFormSelect>
                <CFormFeedback invalid>Please choose a username.</CFormFeedback>
              </CCol>

              <CCol className="mb-3" md={6}>
                <CFormLabel htmlFor="formFile">Default file input example</CFormLabel>
                <CFormInput {...register('image')} type="file" id="formFile" />
              </CCol>
              {/* <div className="mb-3">
                <CFormLabel htmlFor="formFileMultiple">Multiple files input example</CFormLabel>
                <CFormInput type="file" id="formFileMultiple" multiple />
              </div> */}
              <CCol md={5}>
                <CFormSwitch {...register('shareSwitch')} label="Share Data" id="formSwitch" />
              </CCol>
              <CCol md={7}>
                <br />
                <CButton type="submit" color="primary">
                  Submit
                </CButton>
              </CCol>
            </CForm>
            {/* </DocsExample> */}
          </CCardBody>
        </CCard>
      </CCol>
    </CRow>
  )
}

export default FormControl
