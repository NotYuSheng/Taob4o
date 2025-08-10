import React, { useEffect, useState } from 'react';
import './App.css';

function App() {
  const [services, setServices] = useState({});

  useEffect(() => {
    // Test backend services
    const testServices = async () => {
      const serviceUrls = [
        { name: 'User Service', url: '/api/users/health' },
        { name: 'Product Service', url: '/api/products/health' },
        { name: 'Cart Service', url: '/api/cart/health' },
        { name: 'Order Service', url: '/api/orders/health' }
      ];

      const results = {};
      for (const service of serviceUrls) {
        try {
          const response = await fetch(service.url);
          const data = await response.json();
          results[service.name] = { status: 'healthy', data };
        } catch (error) {
          results[service.name] = { status: 'error', error: error.message };
        }
      }
      setServices(results);
    };

    testServices();
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <h1>🛒 Taobao Clone</h1>
        <p>Learning Istio with Microservices</p>
        
        <div className="service-status">
          <h2>Service Health Status</h2>
          {Object.entries(services).map(([name, status]) => (
            <div key={name} className={`service ${status.status}`}>
              <span className="service-name">{name}:</span>
              <span className="service-status-text">{status.status}</span>
              {status.data && <small>{JSON.stringify(status.data)}</small>}
            </div>
          ))}
        </div>
      </header>
    </div>
  );
}

export default App;