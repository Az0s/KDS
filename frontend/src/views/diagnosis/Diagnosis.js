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
  // CSpinner,
  CFormSelect,
  CFormFeedback,
  CRow,
} from '@coreui/react'
import { useForm } from 'react-hook-form'
import axios from 'axios'
import Loading from './Loading'
import Result from './Result'
import { useDispatch } from 'react-redux'

const Diagnosis = () => {
  const dispatch = useDispatch()
  const { register, handleSubmit } = useForm()
  const [loading, setLoading] = React.useState(false)
  const [result, setResult] = React.useState(null)
  const onSubmit = (data) => {
    // store form data in redux store
    dispatch({ type: 'set', form: data })
    let formData = new FormData()
    setLoading(true)
    Object.keys(data).forEach((key) => {
      if (key === 'image') {
        formData.append(key, data[key][0])
      } else {
        formData.append(key, data[key])
      }
    })
    axios
      .post('/api/predict', formData, {
        headers: {
          'Access-Control-Allow-Origin': '*',
        },
      })
      .then((res) => {
        // debugger
        dispatch({
          type: 'set',
          result: res.data,
        })
        setResult(res.data)
        console.log(res.data)
      })
  }

  return (
    <div>
      {!loading && !result && (
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
                    <CFormLabel htmlFor="formName">Name this diagnosis:</CFormLabel>
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
                    <CFormLabel htmlFor="formFile">Upload image:</CFormLabel>
                    <CFormInput {...register('image')} type="file" id="formFile" />
                  </CCol>
                  {/* <div className="mb-3">
                <CFormLabel htmlFor="formFileMultiple">Multiple files input example</CFormLabel>
                <CFormInput type="file" id="formFileMultiple" multiple />
              </div> */}
                  <CCol md={5}>
                    <CFormSwitch
                      {...register('shareSwitch')}
                      label="Share Data with us"
                      id="formSwitch"
                    />
                  </CCol>
                  <CCol md={7}>
                    <br />
                    <CButton type="submit" color="primary" className="text-end">
                      Submit
                    </CButton>
                  </CCol>
                </CForm>
                {/* </DocsExample> */}
              </CCardBody>
            </CCard>
          </CCol>
        </CRow>
      )}
      {loading && !result && <Loading />}
      {result && <Result result={result} />}
    </div>
  )
}

export default Diagnosis
