import React from 'react'
import {
  // CCard,
  // CCardHeader,
  // CCardBody,
  // CButton,
  // CRow,
  // CCol,
  CToast,
  CToastBody,
  // CToastClose,
  CToastHeader,
  CSpinner,
  // CToaster,
} from '@coreui/react'
const Loading = () => {
  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignContent: 'center' }}>
      <CToast
        title="Processing"
        autohide={false}
        visible={true}
        style={{ display: 'inline-block' }}
      >
        <CToastHeader closeButton>
          {/* <svg
            className="rounded me-2"
            width="20"
            height="20"
            xmlns="http://www.w3.org/2000/svg"
            preserveAspectRatio="xMidYMid slice"
            focusable="false"
            role="img"
          >
            <rect width="100%" height="100%" fill="#007aff"></rect>
          </svg> */}
          <CSpinner style={{ margin: '5px' }} component="span" size="sm" aria-hidden="true" />

          <strong className="me-auto"> Processing</strong>
          <small>now</small>
        </CToastHeader>
        <CToastBody>
          Your image is being processed... <br />
          No image uploaded to the server is stored.
        </CToastBody>
      </CToast>
    </div>
  )
}

export default Loading
