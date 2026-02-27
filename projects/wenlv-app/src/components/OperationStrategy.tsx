import { useState } from 'react'

interface Props {
  data: any
  onUpdate: (data: any) => void
  onNext: () => void
  onPrev: () => void
}

const seasonStrategies = [
  { id: 'spring', name: '春季', icon: '🌸', theme: '踏青赏花', activities: ['花海节', '风筝节', '采茶体验'] },
  { id: 'summer', name: '夏季', icon: '☀️', theme: '避暑亲水', activities: ['夜游', '水世界', '露营'] },
  { id: 'autumn', name: '秋季', icon: '🍂', theme: '丰收文化', activities: ['丰收节', '摄影季', '美食节'] },
  { id: 'winter', name: '冬季', icon: '❄️', theme: '温泉暖冬', activities: ['温泉季', '灯会', '年俗活动'] },
]

const marketingChannels = [
  { id: 'douyin', name: '抖音', icon: '🎵', desc: '短视频种草+直播带货', selected: true },
  { id: 'xiaohongshu', name: '小红书', icon: '📕', desc: '图文种草+打卡攻略', selected: true },
  { id: 'wechat', name: '微信生态', icon: '💬', desc: '公众号+小程序+社群', selected: true },
  { id: 'meituan', name: '美团/携程', icon: '🎫', desc: 'OTA平台+票务分销', selected: true },
  { id: 'kol', name: 'KOL合作', icon: '⭐', desc: '达人探店+体验官招募', selected: false },
  { id: 'event', name: '事件营销', icon: '🎯', desc: '造节+话题+热搜', selected: false },
]

const communityTypes = [
  { id: 'membership', name: '会员体系', icon: '👑', desc: '积分+等级+专属权益', features: ['生日特权', '优先预约', '专属折扣'] },
  { id: 'content', name: 'UGC内容', icon: '📸', desc: '鼓励游客创作分享', features: ['打卡奖励', '摄影比赛', '达人计划'] },
  { id: 'activity', name: '社群活动', icon: '🎉', desc: '定期组织主题活动', features: ['主题沙龙', '亲子活动', '会员日'] },
]

export default function OperationStrategy({ data, onUpdate, onNext, onPrev }: Props) {
  const [form, setForm] = useState({
    seasonFocus: data.seasonFocus || [],
    marketingChannels: data.marketingChannels || ['douyin', 'xiaohongshu', 'wechat', 'meituan'],
    communityFeatures: data.communityFeatures || [],
    ipCollaboration: data.ipCollaboration || '',
    differentiation: data.differentiation || '',
  })

  const handleChange = (field: string, value: any) => {
    const newForm = { ...form, [field]: value }
    setForm(newForm)
    onUpdate(newForm)
  }

  const toggleSeason = (id: string) => {
    const current = form.seasonFocus
    const updated = current.includes(id)
      ? current.filter((s: string) => s !== id)
      : [...current, id]
    handleChange('seasonFocus', updated)
  }

  const toggleChannel = (id: string) => {
    const current = form.marketingChannels
    const updated = current.includes(id)
      ? current.filter((c: string) => c !== id)
      : [...current, id]
    handleChange('marketingChannels', updated)
  }

  const toggleCommunity = (id: string) => {
    const current = form.communityFeatures
    const updated = current.includes(id)
      ? current.filter((c: string) => c !== id)
      : [...current, id]
    handleChange('communityFeatures', updated)
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <div className="mb-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-2">⚡ 运营策略</h2>
        <p className="text-gray-600">制定四季运营、营销推广和社群运营策略</p>
      </div>

      <div className="space-y-6">
        {/* 四季运营 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            重点发力季节（可多选）
          </label>
          <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
            {seasonStrategies.map((season) => (
              <button
                key={season.id}
                onClick={() => toggleSeason(season.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.seasonFocus.includes(season.id)
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-2xl">{season.icon}</span>
                  <span className="font-medium text-gray-800">{season.name}</span>
                </div>
                <div className="text-sm text-orange-600 font-medium mb-1">{season.theme}</div>
                <div className="text-xs text-gray-500">{season.activities.join('、')}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 营销渠道 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            数字营销渠道（可多选）
          </label>
          <div className="grid grid-cols-2 md:grid-cols-3 gap-3">
            {marketingChannels.map((channel) => (
              <button
                key={channel.id}
                onClick={() => toggleChannel(channel.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.marketingChannels.includes(channel.id)
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="flex items-center gap-2 mb-2">
                  <span className="text-2xl">{channel.icon}</span>
                  <span className="font-medium text-gray-800">{channel.name}</span>
                </div>
                <div className="text-xs text-gray-500">{channel.desc}</div>
              </button>
            ))}
          </div>
        </div>

        {/* 社群运营 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-3">
            社群运营体系（可多选）
          </label>
          <div className="grid grid-cols-3 gap-3">
            {communityTypes.map((type) => (
              <button
                key={type.id}
                onClick={() => toggleCommunity(type.id)}
                className={`p-4 rounded-xl border-2 text-left transition-all ${
                  form.communityFeatures.includes(type.id)
                    ? 'border-orange-500 bg-orange-50'
                    : 'border-gray-100 hover:border-orange-200'
                }`}
              >
                <div className="text-2xl mb-1">{type.icon}</div>
                <div className="font-medium text-gray-800 mb-1">{type.name}</div>
                <div className="text-xs text-gray-500 mb-2">{type.desc}</div>
                <div className="flex flex-wrap gap-1">
                  {type.features.map((f) => (
                    <span key={f} className="text-xs bg-white px-2 py-0.5 rounded">{f}</span>
                  ))}
                </div>
              </button>
            ))}
          </div>
        </div>

        {/* IP 合作 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            IP 联名/合作计划
          </label>
          <textarea
            value={form.ipCollaboration}
            onChange={(e) => handleChange('ipCollaboration', e.target.value)}
            placeholder="例如：与知名动漫IP合作打造主题区、与非遗传承人合作..."
            rows={3}
            className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent resize-none"
          />
        </div>

        {/* 差异化竞争 */}
        <div>
          <label className="block text-sm font-medium text-gray-700 mb-2">
            与竞品的差异化优势
          </label>
          <textarea
            value={form.differentiation}
            onChange={(e) => handleChange('differentiation', e.target.value)}
            placeholder="例如：独有的文化资源、创新的体验形式、更优的地理位置..."
            rows={3}
            className="w-full px-4 py-3 border border-gray-200 rounded-lg focus:ring-2 focus:ring-orange-500 focus:border-transparent resize-none"
          />
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
          生成策划方案 →
        </button>
      </div>
    </div>
  )
}
