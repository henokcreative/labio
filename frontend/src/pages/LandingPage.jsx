import React from "react";
import "./LandingPage.css";
import ContactForm from "../components/ContactForm";


const projects = [
  { id: 1, title: "Photography Project", image: "https://via.placeholder.com/300x200?text=Photo+Project" },
  { id: 2, title: "Videography Project", image: "https://via.placeholder.com/300x200?text=Video+Project" },
  { id: 3, title: "Web Design Project", image: "https://via.placeholder.com/300x200?text=Web+Project" },
  { id: 4, title: "Print Design Project", image: "https://via.placeholder.com/300x200?text=Print+Project" },
];

const LandingPage = () => {
  const scrollToSection = (id) => {
    const element = document.getElementById(id);
    if (element) {
      element.scrollIntoView({ behavior: "smooth" });
    }
  };

  return (
    <div className="landing-page">
      {/* Navigation */}
      <nav className="navbar">
        <ul>
          <li onClick={() => scrollToSection("hero")}>Home</li>
          <li onClick={() => scrollToSection("projects")}>Portfolio</li>
          <li onClick={() => scrollToSection("about")}>About</li>
          <li onClick={() => scrollToSection("contact")}>Contact</li>
        </ul>
      </nav>

      {/* Hero Section */}
      <header className="hero" id="hero">
        <h1>Labio</h1>
        <p>Digital Production | Photography | Videography | Web Development</p>
        <button onClick={() => scrollToSection("projects")}>View Portfolio</button>
      </header>

      {/* Project Gallery */}
      <section className="projects" id="projects">
        <h2>Recent Work</h2>
        <div className="project-grid">
          {projects.map((project) => (
            <div key={project.id} className="project-card">
              <img src={project.image} alt={project.title} />
              <h3>{project.title}</h3>
            </div>
          ))}
        </div>
      </section>

      {/* About Section (Placeholder) */}
      <section className="about" id="about">
        <h2>About Labio</h2>
        <p>We specialize in digital production, photography, videography, and web development for small businesses.</p>
      </section>

      {/* Contact Section (Placeholder) */}
      <section className="contact" id="contact">
        <h2>Contact Us</h2>
        <p>Client forms and requests will appear here soon!</p>
        <section className="contact" id="contact">
  <ContactForm />
</section>
        
      </section>
    </div>
  );
};

export default LandingPage;
