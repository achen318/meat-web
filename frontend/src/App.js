import './App.css';

import { Table, TableCell, TableHead, TableRow } from '@mui/material';

import CamFeed from './components/CamFeed';
import { useState } from 'react';

export default function App() {
  const [emotion, setEmotion] = useState('neutral');
  const [confidence, setConfidence] = useState(0);

  return (
    <div className="App">
      <h1>Multimodal Emotion Analysis Technology</h1>

      <CamFeed />

      <Table sx={{ maxWidth: 600 }}>
        <TableHead>
          <TableRow>
            <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>
              Emotion
            </TableCell>
            <TableCell sx={{ fontWeight: 'bold', color: 'white' }}>
              Confidence
            </TableCell>
          </TableRow>
        </TableHead>

        <TableRow>
          <TableCell>{emotion}</TableCell>
          <TableCell>{confidence}</TableCell>
        </TableRow>
      </Table>

      <footer className="App-footer">
        <p>Created by: Andrew Liu, Anthony Chen, Eric Lin, Tracey Lin</p>
        <p>Mentored by: Hima Sajeev</p>
      </footer>
    </div>
  );
}
