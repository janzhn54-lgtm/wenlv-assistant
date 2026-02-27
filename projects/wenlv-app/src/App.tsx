import { useState } from 'react'
import ProjectPositioning from './components/ProjectPositioning'
import BusinessPlanning from './components/BusinessPlanning'
import OperationStrategy from './components/OperationStrategy'
import OutputResult from './components/OutputResult'
import './index.css'

type Step = 'positioning' | 'business' | 'operation' | 'output'

function App() {
  const [currentStep, setCurrentStep] = useState<Step>('positioning')
  const [formData, setFormData] = useState({
    positioning: {},
    business: {},
    operation: {}
  })

  const steps = [
    { id: 'positioning' as Step, title: '项目定位', icon: '🎯' },
    { id: 'business' as Step, title: '业态规划', icon: '🏗️' },
    { id: 'operation' as Step, title: '运营策略', icon: '⚡' },
    { id: 'output' as Step, title: '生成方案', icon: '📄' },
  ]

  const updateFormData = (step: Step, data: any) => {
    setFormData(prev => ({ ...prev, [step]: data }))
  }

  const renderStep = () => {
    switch (currentStep) {
      case 'positioning':
        return <ProjectPositioning 
          data={formData.positioning} 
          onUpdate={(data) => updateFormData('positioning', data)}
          onNext={() => setCurrentStep('business')}
        />
      case 'business':
        return <BusinessPlanning 
          data={formData.business}
          onUpdate={(data) => updateFormData('business', data)}
          onNext={() => setCurrentStep('operation')}
          onPrev={() => setCurrentStep('positioning')}
        />
      case 'operation':
        return <OperationStrategy 
          data={formData.operation}
          onUpdate={(data) => updateFormData('operation', data)}
          onNext={() => setCurrentStep('output')}
          onPrev={() => setCurrentStep('business')}
        />
      case 'output':
        return <OutputResult 
          formData={formData}
          onPrev={() => setCurrentStep('operation')}
        />
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-br from-orange-50 to-amber-50">
      {/* Header */}
      <header className="bg-white shadow-sm border-b border-orange-100">
        <div className="max-w-6xl mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center gap-3">
              <div className="w-10 h-10 bg-gradient-to-br from-orange-500 to-amber-600 rounded-lg flex items-center justify-center text-white text-xl">
                🏛️
              </div>
              <div>
                <h1 className="text-xl font-bold text-gray-800">文旅策划生成器</h1>
                <p className="text-sm text-gray-500">专业文旅项目策划方案一键生成</p>
              </div>
            </div>
            <div className="text-sm text-gray-500">
              让策划更简单 · 让创意更有价值
            </div>
          </div>
        </div>
      </header>

      {/* Progress Steps */}
      <div className="bg-white border-b border-orange-100">
        <div className="max-w-6xl mx-auto px-4 py-6">
          <div className="flex items-center justify-center">
            {steps.map((step, index) => (
              <div key={step.id} className="flex items-center">
                <button
                  onClick={() => setCurrentStep(step.id)}
                  className={`flex items-center gap-2 px-4 py-2 rounded-full transition-all ${
                    currentStep === step.id
                      ? 'bg-orange-500 text-white shadow-lg'
                      : 'bg-gray-100 text-gray-600 hover:bg-gray-200'
                  }`}
                >
                  <span>{step.icon}</span>
                  <span className="font-medium">{step.title}</span>
                </button>
                {index < steps.length - 1 && (
                  <div className="w-8 h-0.5 bg-gray-200 mx-2" />
                )}
              </div>
            ))}
          </div>
        </div>
      </div>

      {/* Main Content */}
      <main className="max-w-6xl mx-auto px-4 py-8">
        {renderStep()}
      </main>

      {/* Footer */}
      <footer className="bg-white border-t border-orange-100 mt-auto">
        <div className="max-w-6xl mx-auto px-4 py-4 text-center text-sm text-gray-500">
          文旅策划生成器 · 基于拈花湾、阿那亚等标杆案例方法论
        </div>
      </footer>
    </div>
  )
}

export default App
