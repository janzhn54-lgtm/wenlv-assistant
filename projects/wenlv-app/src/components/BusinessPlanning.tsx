import { useState } from 'react'

interface Props {
  data: any
  onUpdate: (data: any) => void
  onNext: () => void
  onPrev: () => void
}

const attractionTypes = [
  { id: 'landmark', name: '地标景观', icon: '🏛️', examples: '白塔、摩天轮、观景塔' },
  { id: 'performance', name: '演艺活动', icon: '🎭', examples: '实景演出、光影秀、巡游' },
  { id: 'experience', name: '沉浸体验', icon: '🎪', examples: '剧本杀、VR体验、互动装置' },
  { id: 'museum', name: '文化场馆', icon: '🏺', examples: '博物馆、美术馆、非遗馆' },
  { id: 'nature', name: '自然景观', icon: '🌲', examples: '花海、湿地、森林公园' },
  { id: 'night', name: '夜间项目', icon: '🌙', examples: '灯光秀、夜市、夜演' },
]

const businessTypes = [
  { id: 'catering', name: '餐饮', icon: '🍜', ratio: 30, desc: '地方特色+连锁品牌+网红餐饮' },
  { id: 'retail', name: '零售', icon: '🛍️', ratio: 25, desc: '文创产品+特产+生活方式' },
  { id: 'accommodation', name: '住宿', icon: '🏨', ratio: 20, desc: '精品酒店+民宿+露营地' },
  { id: 'entertainment', name: '娱乐', icon: '🎮', ratio: 15, desc: '亲子+潮玩+休闲体验' },
  { id: 'service', name: '服务', icon: '💁', ratio: 10, desc: '游客中心+交通+配套设施' },
]

const circulationPatterns = [
  { id: 'loop', name: '环线式', icon: '🔄', desc: '游客沿环形路线游览，适合中小型项目' },
  { id: 'spine', name: '主轴式', icon: '📍', desc: '一条主街串联各节点，如古镇街道' },
  { id: 'cluster', name: '组团式', icon: '🔷', desc: '多个主题组团，适合大型综合项目' },
  { id: 'network', name: '网络式', icon: '🔗', desc: '多路径自由探索，适合开放式景区' },
]

export default function BusinessPlanning({ data, onUpdate, onNext, onPrev }: Props) {
  const [form, setForm] = useState({
    coreAttraction: data.coreAttraction || [],
    businessRatio: data.businessRatio || {
      catering: 30,
      retail: 25,
      accommodation: 20,
      entertainment: 15,
      service: 10,
    },
    circulation: data.circulation || '',
    stayDuration: data.stayDuration || '',
    ticketPrice: data.ticketPrice || '',
    annualCapacity: data.annualCapacity || '',
  })

  const handleChange = (field: string, value: any) => {
    const newForm = { ...form, [field]: value }
    setForm(newForm)
    onUpdate(newForm)
  }

  const toggleAttraction = (id: string) => {
    const current = form.coreAttraction
    const updated = current.includes(id)
      ? current.filter((a: string) => a !== id)
      : [...current, id]
    handleChange('coreAttraction', updated)
  }

  const updateRatio = (type: string, value: number) => {
    handleChange('businessRatio', { ...form.businessRatio, [type]: value })
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">🏗️ 业态规划</h2>
        <p className="text-gray-600">设计核心吸引物、业态配比和游客动线</p>
      </div>

      <div className="space-y-6">
        {/* 核心吸引物 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            核心吸引物（可多选）
          </label>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
            {attractionTypes.map((type) => (
              <button
                key={type.id}
                onClick={() => toggleAttraction(type.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.coreAttraction.includes(type.id)
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="text-2xl mb-1">{type.icon}</div>
                <div className="font-medium text-gray-800">{type.name}</div>
                <div className="text-xs text-gray-500 mt-1">{type.examples}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 业态配比 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            业态配比调整
          </label>
          <div className="space-y-4 bg-gray-50 p-4 rounded-xl">
            {businessTypes.map((type) => (
              <div key={type.id} className="flex items-center gap-4">
                <div className="w-8 text-2xl">{type.icon}</div>
                <div className="flex-1">
                  <div className="flex justify-between mb-1">
                    <span className="font-medium text-gray-700">{type.name}</span>
                    <span className="text-orange-600 font-bold">{form.businessRatio[type.id]}%</span>
                  </div>
                  <input
                    type="range"
                    min="0"
                    max="50"
                    value={form.businessRatio[type.id]}
                    onChange={(e) => updateRatio(type.id, parseInt(e.target.value))}
                    className="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-orange-500"
                  />
                  <div className="text-xs text-gray-500 mt-1">{type.desc}</div>
                </div>
              </div>
            ))}
          </div>
        </div>

        {/* 动线设计 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            游客动线设计
          </label>
          <div className="grid grid-cols-2 gap-3">
            {circulationPatterns.map((pattern) => (
              <button
                key={pattern.id}
                onClick={() => handleChange('circulation', pattern.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.circulation === pattern.id
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="text-2xl mb-1">{pattern.icon}</div>
                <div className="font-medium text-gray-800">{pattern.name}</div>
                <div className="text-xs text-gray-500 mt-1">{pattern.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 运营指标 */}
        <div className="grid grid-cols-3 gap-4">
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              停留时长（小时）
            </label>
            <select
              value={form.stayDuration}
              onChange={(e) => handleChange('stayDuration', e.target.value)}
              className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500"
            >
              <option value="">请选择</option>
              <option value="2-4">2-4小时（半日游）</option>
              <option value="4-8">4-8小时（一日游）</option>
              <option value="1-2d">1-2天（过夜游）</option>
              <option value="3d+">3天以上（度假游）</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              门票价格区间
            </label>
            <select
              value={form.ticketPrice}
              onChange={(e) => handleChange('ticketPrice', e.target.value)}
              className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500"
            >
              <option value="">请选择</option>
              <option value="free">免费开放</option>
              <option value="low">50元以下</option>
              <option value="mid">50-150元</option>
              <option value="high">150-300元</option>
              <option value="premium">300元以上</option>
            </select>
          </div>
          <div>
            <label className="block text-sm font-medium text-gray-700 mb-2">
              年游客容量（万人次）
            </label>
            <select
              value={form.annualCapacity}
              onChange={(e) => handleChange('annualCapacity', e.target.value)}
              className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500"
            >
              <option value="">请选择</option>
              <option value="10">10万以下</option>
              <option value="50">10-50万</option>
              <option value="100">50-100万</option>
              <option value="300">100-300万</option>
              <option value="500">300万以上</option>
            </select>
          </div>
        </div>
      </div>

      {/* 按钮组 */}
      <div className="mt-8 flex justify-between">
        <button
          onClick={onPrev}
          className="px-6 py-3 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-all"
        >
          ← 上一步
        </button>
        <button
          onClick={onNext}
          className="px-8 py-3 bg-gradient-to-r from-orange-500 to-amber-600 text-white font-medium rounded-lg hover:shadow-lg transition-all"
        >
          下一步：运营策略 →
        </button>
      </div>
    </div>
  )
}
