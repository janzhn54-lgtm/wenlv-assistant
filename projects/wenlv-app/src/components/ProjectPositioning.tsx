import { useState } from 'react'

interface Props {
  data: any
  onUpdate: (data: any) => void
  onNext: () => void
}

const locationTypes = [
  { id: 'watertown', name: '江南水乡', icon: '🏘️', desc: '古镇、水系、慢生活' },
  { id: 'mountain', name: '山水生态', icon: '⛰️', desc: '自然、康养、户外' },
  { id: 'cultural', name: '文化古迹', icon: '🏛️', desc: '历史、人文、研学' },
  { id: 'coastal', name: '滨海度假', icon: '🏖️', desc: '海洋、休闲、度假' },
  { id: 'rural', name: '田园乡村', icon: '🌾', desc: '农业、民俗、亲子' },
  { id: 'urban', name: '城市更新', icon: '🏙️', desc: '工业遗产、文创园' },
]

const targetGroups = [
  { id: 'family', name: '亲子家庭', icon: '👨‍👩‍👧‍👦', desc: '3-12岁儿童家庭，注重安全与教育' },
  { id: 'youth', name: 'Z世代青年', icon: '🎒', desc: '18-30岁，追求体验与社交分享' },
  { id: 'silver', name: '银发族', icon: '👴', desc: '55岁+，注重康养与品质' },
  { id: 'business', name: '商务客群', icon: '💼', desc: '企业团建、会议、商务休闲' },
  { id: 'couple', name: '情侣/蜜月', icon: '💕', desc: '浪漫体验、打卡拍照' },
  { id: 'culture', name: '文化爱好者', icon: '📚', desc: '深度文化体验、研学' },
]

const positioningTypes = [
  { id: 'ip', name: '文化IP型', icon: '🎭', desc: '如拈花湾（禅意）、大唐不夜城（唐文化）' },
  { id: 'ecology', name: '生态康养型', icon: '🌿', desc: '如莫干山、安吉，主打自然与康养' },
  { id: 'community', name: '社群运营型', icon: '👥', desc: '如阿那亚，用社群凝聚高粘性用户' },
  { id: 'immersive', name: '沉浸体验型', icon: '🎪', desc: '如只有河南，戏剧+文旅深度融合' },
  { id: 'rural', name: '田园综合型', icon: '🏡', desc: '如袁家村，民俗+美食+住宿' },
  { id: 'night', name: '夜间经济型', icon: '🌙', desc: '灯光秀、夜市、夜演、夜宿' },
]

export default function ProjectPositioning({ data, onUpdate, onNext }: Props) {
  const [form, setForm] = useState({
    projectName: data.projectName || '',
    location: data.location || '',
    locationType: data.locationType || '',
    targetGroup: data.targetGroup || [],
    positioning: data.positioning || '',
    coreTheme: data.coreTheme || '',
    competitors: data.competitors || '',
  })

  const handleChange = (field: string, value: any) => {
    const newForm = { ...form, [field]: value }
    setForm(newForm)
    onUpdate(newForm)
  }

  const toggleTargetGroup = (id: string) => {
    const current = form.targetGroup
    const updated = current.includes(id)
      ? current.filter((g: string) => g !== id)
      : [...current, id]
    handleChange('targetGroup', updated)
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">🎯 项目定位</h2>
        <p className="text-gray-600">明确项目的文化基因、目标客群和差异化定位</p>
      </div>

      <div className="space-y-6">
        {/* 项目名称 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            项目名称
          </label>
          <input
            type="text"
            value={form.projectName}
            onChange={(e) => handleChange('projectName', e.target.value)}
            placeholder="例如：绍兴XX文旅综合体"
            className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent"
          />
        </div>

        {/* 地理位置 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            项目位置
          </label>
          <input
            type="text"
            value={form.location}
            onChange={(e) => handleChange('location', e.target.value)}
            placeholder="例如：浙江省绍兴市柯桥区"
            className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent"
          />
        </div>

        {/* 地域类型 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            地域资源类型
          </label>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
            {locationTypes.map((type) => (
              <button
                key={type.id}
                onClick={() => handleChange('locationType', type.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.locationType === type.id
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="text-2xl mb-1">{type.icon}</div>
                <div className="font-medium text-gray-800">{type.name}</div>
                <div className="text-xs text-gray-500 mt-1">{type.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 目标客群 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            目标客群（可多选）
          </label>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
            {targetGroups.map((group) => (
              <button
                key={group.id}
                onClick={() => toggleTargetGroup(group.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.targetGroup.includes(group.id)
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="text-2xl mb-1">{group.icon}</div>
                <div className="font-medium text-gray-800">{group.name}</div>
                <div className="text-xs text-gray-500 mt-1">{group.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 定位类型 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            项目定位类型
          </label>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
            {positioningTypes.map((type) => (
              <button
                key={type.id}
                onClick={() => handleChange('positioning', type.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.positioning === type.id
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="text-2xl mb-1">{type.icon}</div>
                <div className="font-medium text-gray-800">{type.name}</div>
                <div className="text-xs text-gray-500 mt-1">{type.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 核心主题 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            核心文化主题
          </label>
          <input
            type="text"
            value={form.coreTheme}
            onChange={(e) => handleChange('coreTheme', e.target.value)}
            placeholder="例如：江南水韵、越国文化、黄酒文化..."
            className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent"
          />
        </div>

        {/* 竞品 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            主要竞品/对标项目
          </label>
          <textarea
            value={form.competitors}
            onChange={(e) => handleChange('competitors', e.target.value)}
            placeholder="例如：乌镇、西塘、拈花湾..."
            rows={3}
            className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent resize-none"
          />
        </div>
      </div>

      {/* 下一步按钮 */}
      <div className="mt-8 flex justify-end">
        <button
          onClick={onNext}
          className="px-8 py-3 bg-gradient-to-r from-orange-500 to-amber-600 text-white font-medium rounded-lg hover:shadow-lg transition-all"
        >
          下一步：业态规划 →
        </button>
      </div>
    </div>
  )
}
