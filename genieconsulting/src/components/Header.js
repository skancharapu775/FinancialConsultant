import { AppBar, Toolbar, IconButton, Typography, Stack, Button } from '@mui/material';
import Box from '@mui/material/Box';
import '../App.css';

export default function Header() {
    return (
        <Box sx={{ flexGrow: 1 }}>
            <div className='header'>
                <AppBar style={{ background: '#1a1a1a' }} position='static'>
                    <Toolbar>
                        <Typography variant='h6' component='div' sx={{ flexGrow: 0, fontWeight: 'bold' }}>
                            GenieConsultant
                        </Typography>
                    </Toolbar>
                </AppBar>
            </div>
        </Box>
    )
}