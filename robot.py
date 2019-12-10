import wpilib
import wpilib.drive
import wpilib.buttons
import ctre

class Robot(wpilib.TimedRobot):
    
    def robotInit(self):
        self.joystick = wpilib.Joystick(0)
        self.driveButton = wpilib.buttons.JoystickButton(self.joystick, 2)
        
        self.lMotor = ctre.WPI_VictorSPX(1)
        self.rMotor = ctre.WPI_VictorSPX(2)
        
        self.driveTrain = wpilib.drive.DifferentialDrive(self.lMotor, self.rMotor)
        self.driveTrain.setRightSideInverted(False)

        self.tankDrive = False

    def teleopPeriodic(self):

        if self.tankDrive:
            self.driveTrain.tankDrive(-self.joystick.getAxis(1),self.joystick.getAxis(4))

        else:
            self.driveTrain.arcadeDrive(self.joystick.getAxis(0), self.joystick.getAxis(1))

        #TankDrive Button
        if (self.joystick.getRawButtonPressed(1)):
            self.tankDrive = not self.tankDrive

if __name__ == '__main__':
    wpilib.run(Robot)



