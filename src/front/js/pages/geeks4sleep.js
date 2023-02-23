import React from 'react'
import GeeksList from '../component/geeksList'
import GeeksRoom from '../component/geeksRoom'

export default function Geeks4sleep() {
  return (
    <div>
        <Route element={<GeeksList />} path="/geeks4sleep/list" />
        <Route element={<GeeksRoom />} path="/geeks4sleep/room" />
    </div>
  )
}
