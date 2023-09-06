import React, { useState } from 'react';
import './App.css';

function App() {
  const [formData, setFormData] = useState({
    username: '',
    gender: '',
    interests: [],
    country: ''
  });

  const handleChange = (e) => {
    const { name, value, type, checked } = e.target;

    if (type === 'checkbox') {
      setFormData((prevData) => ({
        ...prevData,
        interests: checked
          ? [...prevData.interests, value]
          : prevData.interests.filter((interest) => interest !== value)
      }));
    } else {
      setFormData((prevData) => ({ ...prevData, [name]: value }));
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    alert(JSON.stringify(formData, null, 2));
  };

  const handleReset = () => {
    setFormData({
      username: '',
      password: '',
      gender: '',
      interests: [],
      country: ''
    });
    alert("Form has been reset.");
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSubmit(e);
    } else if (e.key === 'Escape') {
      handleReset();
    }
  };

  return (
    <div className="container" onKeyDown={handleKeyDown}>
      <form onSubmit={handleSubmit}>
        <label>
          Username:
          <input
            type="text"
            name="username"
            value={formData.username}
            onChange={handleChange}
          />
        </label>
        <label>
          Password:
          <input
            type="password"
            name="password"
            value={formData.password}
            onChange={handleChange}
          />
        </label>
        <div>
          Gender:
          <label>
            <input
              type="radio"
              name="gender"
              value="male"
              checked={formData.gender === 'male'}
              onChange={handleChange}
            />
            Male
          </label>
          <label>
            <input
              type="radio"
              name="gender"
              value="female"
              checked={formData.gender === 'female'}
              onChange={handleChange}
            />
            Female
          </label>
        </div>
        <div>
          Interests:
          <label>
            <input
              type="checkbox"
              name="interests"
              value="coding"
              checked={formData.interests.includes('coding')}
              onChange={handleChange}
            />
            Coding
          </label>
          <label>
            <input
              type="checkbox"
              name="interests"
              value="music"
              checked={formData.interests.includes('music')}
              onChange={handleChange}
            />
            Music
          </label>
        </div>
        <label>
          Country:
          <select
            name="country"
            value={formData.country}
            onChange={handleChange}
          >
            <option value="">--Select--</option>
            <option value="USA">China</option>
            <option value="India">India</option>
            <option value="UK">UK</option>
            <option value="UK">USA</option>
          </select>
        </label>
        <button type="submit">Submit</button>
        <button type="button" onClick={handleReset}>
          Reset
        </button>
      </form>
    </div>
  );
}

export default App;
