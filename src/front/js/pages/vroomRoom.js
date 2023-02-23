import React from 'react'
import VroomList from '../component/vroomList'
import VroomRoomRoom from '../component/vroomRoomRoom'

export default function VroomRoom() {
  return (
    <div>
        <Route element={<VroomList />} path="/vroom_room/list" />
        <Route element={<VroomRoomRoom />} path="/vroom_room/room" />
    </div>
  )
}
