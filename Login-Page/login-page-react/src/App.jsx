import React, { useState } from "react";
import profilePicture from "./img/defaultProfilePicture.png";
import "./App.css";

function App() {
  const [isVisible, setVisible] = useState(false); /*false*/

  const [moveTop, setMoveTop] = useState("0px") /*0px*/
  const [moveBottom, setMoveBottom] = useState("750px") /*750px*/
  /*                                             ↓ Defalut Data ↑              */
  const [VisibleRegister, setVisibleRegister] = useState('block') /*block*/
  const [ResizeWrapperHeight, setResizeWrapperHeight] = useState('750px') /*750px*/
  const [VisibleResetPopup, setVisibleResetPopup] = useState(false) /*false*/

  const [checkEmailPosition, setCheckEmailPosition] = useState(true) /*true*/
  const [checkPasswordPosition, setCheckCodePosition] = useState(false) /*false*/
  const [newPasswordPosition, setNewPasswordPosition] = useState(false) /*false*/

  /* Functions for reseting inputs data */

  function reset() {
    setVisibleRegister('block')
    setResizeWrapperHeight("750px")
    setVisibleResetPopup(false)

    resetForms()
  }

  function resetForms() {
    setLoginData({
      userOrEmail: "",
      password: ""
    });
    setRegisterData({
      user: "",
      email: "",
      password: "",
      confirmPassword: ""
    });
    setResetData({
      email: "",
      code: "",
      password: "",
      confirmPassword: ""
    });

    setCheckEmailPosition(true)
    setCheckCodePosition(false)
    setNewPasswordPosition(false)
  }

  /* Functions for background on and off */

  function BackgroundFalse() {
    setVisible(false);
    reset();
  };

  function BackgroundTrue() {
    setVisible(true);
    reset()
  };

  /* Functions for handaling transition betwen sign in and sign up popups*/

  function registerOn() {
    setMoveTop('-750px')
    setMoveBottom("0px")
    reset()
  }

  function registerOff() {
    setMoveTop('0px')
    setMoveBottom('750px')
    reset()
  }

  let stylespopup = {
    display: `${VisibleRegister}`
  };

  let stylesBottom = {
    transform: `translateY(${moveBottom})`
  };

  /* Functions for handaling resetPassword popup */

  function HiddenRegisterFunc() {
    setVisibleRegister('none')
    resizeWrapperHeightFunc('300px')
    setVisibleResetPopup(true)
    resetForms()
  }

  function VisibleRegisterFunc() {
    setVisibleResetPopup(false)
    resizeWrapperHeightFunc('750px')
    setVisibleRegister('block')
    resetForms()
  }

  function resizeWrapperHeightFunc(size) {
    setResizeWrapperHeight(size)
  }

  /* Functions for handaling inputs data */

  const [loginData, setLoginData] = useState({
    userOrEmail: "",
    password: ""
  });

  const [registerData, setRegisterData] = useState({
    user: "",
    email: "",
    password: "",
    confirmPassword: ""
  });

  const [resetData, setResetData] = useState({
    email: "",
    code: "",
    password: "",
    confirmPassword: ""
  });

  const handleInputChangeLogin = (event) => {
    setLoginData((prevState) => ({
      ...prevState,
      [event.target.name]: event.target.value,
    }));
  };

  const handleInputChangeRegister = (event) => {
    setRegisterData((prevState) => ({
      ...prevState,
      [event.target.name]: event.target.value,
    }));
  };

  const handleInputChangeResetPassword = (event) => {
    setResetData((prevState) => ({
      ...prevState,
      [event.target.name]: event.target.value,
    }));
  };

  /* Functions for transition betwen resetPopup */

  function toEmail() {
    setCheckEmailPosition(true)
    setCheckCodePosition(false)
    setNewPasswordPosition(false)
  }

  function toCode() {
    setCheckEmailPosition(false)
    setCheckCodePosition(true)
    setNewPasswordPosition(false)
    setResizeWrapperHeight('300px')
  }

  function toNewPassword() {
    setCheckEmailPosition(false)
    setCheckCodePosition(false)
    setNewPasswordPosition(true)
    setResizeWrapperHeight('550px')
  }

  /* Functions in progress */

  function checkEmail() {



    toCode()
  }


  function checkCode() {



    toNewPassword()
  }

  function checkNewPassword() {



    reset()
  }

  /* Functions in progress */

  return (
    <div className="App">
      <nav className="navBar">
        <div className="navBarLogo">Logo</div>
        <div className="navBarContent">
          <div className="home">
            <p className="a" style={{ color: "#000" }}>Home</p>
          </div>
          <div className="contacts">
            <p className="a" style={{ color: "#000" }}>Contacts</p>
          </div>
          <div className="about">
            <p className="a" style={{ color: "#000" }}>About</p>
          </div>
          <div className="signIn" id="signIn" onClick={BackgroundTrue}>
            Sign In
          </div>
          <img className="profilePicture" src={profilePicture} alt="Error" />
        </div>
      </nav>



      <form id="form">
        <div className="tempText">You Need to Sign In</div>
      </form>

      <div className="background" id="background" onClick={BackgroundFalse} style={{ display: isVisible ? 'block' : 'none' }}></div>



      <div className="wrapper" style={{ display: isVisible ? 'block' : 'none', height: ResizeWrapperHeight, }}>
        <div className="Popup" style={stylespopup}>


          <div className="loginPopup" style={{ transform: `translateY(${moveTop})` }}>
            <p className="mainText">Sign In</p>
            <div className="inputs">
              <input type="text" placeholder='Enter user or email' name="userOrEmail" onChange={handleInputChangeLogin} value={loginData.userOrEmail} />
              <input type="password" placeholder='Enter password' name="password" onChange={handleInputChangeLogin} value={loginData.password} />
            </div>
            <div className="forgotPassword">Forgot your password?
              <br />
              <div className="aAllDiv">
                <p className="a1" onClick={HiddenRegisterFunc}>Try other options!</p>
              </div>
            </div>
            <div className="btn">
              <button className="loginBtn">Continue</button>
            </div>
            <div className="registerFromLogin">Don't have an account?
              <div className="aAllDiv">
                <p className="a2" onClick={registerOn}>Let's Sign Up!</p>
              </div>
            </div>
          </div>


          <div className="registerPopup" style={stylesBottom}>
            <p className="mainTextRegister">Sign Up</p>
            <div className="inputs">
              <input type="text" placeholder='Enter user' name="user" onChange={handleInputChangeRegister} value={registerData.user} />
              <input type="text" placeholder='Enter email' name="email" onChange={handleInputChangeRegister} value={registerData.email} />
              <input type="password" placeholder='Enter password' name="password" onChange={handleInputChangeRegister} value={registerData.password} />
              <input type="password" placeholder='Confirm password' name="confirmPassword" onChange={handleInputChangeRegister} value={registerData.confirmPassword} />
            </div>
            <div className="btn">
              <button className="loginBtn">Continue</button>
            </div>
            <div className="LoginFromRegister">Don't have an account?
              <div className="aAllDiv">
                <p className="a3" id="signInToRegister" onClick={registerOff}>Let's Sign In!</p>
              </div>
            </div>
          </div>
        </div>



        <div className="resetPopup" style={{ display: VisibleResetPopup ? "block" : 'none' }}>


          <div className="enterEmail" style={{ display: checkEmailPosition ? 'block' : 'none' }}>
            <div className="inputs">
              <input type="text" placeholder='Enter email' name="email" onChange={handleInputChangeResetPassword} value={resetData.email} />
            </div>
            <div className="btn">
              <button className="loginBtn" id="checkEmail" onClick={checkEmail}>Continue</button>
            </div>
            <div className="alignBack">
              <p onClick={VisibleRegisterFunc} className="back">Back</p>
            </div>
          </div>


          <div className="enterCode" style={{ display: checkPasswordPosition ? 'block' : 'none' }}>
            <div className="inputs">
              <input type="password" placeholder='Enter code' name="email" onChange={handleInputChangeResetPassword} value={resetData.code} />
            </div>
            <div className="btn">
              <button className="loginBtn" id="checkPassword" onClick={checkCode}>Continue</button>
            </div>
            <div className="alignBack">
              <p onClick={toEmail} className="back">Back</p>
            </div>
          </div>


          <div className="newPassword" style={{ display: newPasswordPosition ? 'block' : 'none' }}>
            <p className="mainTextRessetPassword">New Password</p>
            <div className="inputs">
              <input type="password" placeholder='Enter password' name="email" onChange={handleInputChangeResetPassword} value={resetData.password} />
              <input type="password" placeholder='Enter password' name="email" onChange={handleInputChangeResetPassword} value={resetData.confirmPassword} />
            </div>
            <div className="btn">
              <button className="loginBtn" id="checkPassword" onClick={checkNewPassword}>Continue</button>
            </div>
          </div>


        </div>
      </div>
    </div>
  );
}

export default App;