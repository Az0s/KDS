import React from 'react'
import { render, screen } from '@testing-library/react'
import Diagnosis from './Diagnosis'
import { Provider } from 'react-redux'
import { store } from '../../store'

test('renders basic submit form', async () => {
  render(
    <Provider store={store}>
      <Diagnosis />
    </Provider>,
  )
  expect(screen.getAllByPlaceholderText('Input Name')).toBeInTheDocument()
})
 