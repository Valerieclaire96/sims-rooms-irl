import React from 'react'
import ScholarsList from '../component/scholarsList'
import ScholarsRooms from '../component/scholarsRooms'

export default function ScholarsStudy() {
  return (
    <div>
      <Route element={<ScholarsList />} path="/scholars_study/list" />
      <Route element={<ScholarsRooms />} path="/scholars_study/room" />
    </div>
  )
}
