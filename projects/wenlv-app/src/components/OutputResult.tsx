import { useState } from 'react'

interface Props {
  formData: {
    positioning: any
    business: any
    operation: any
  }
  onPrev: () => void
}

export default function OutputResult({ formData, onPrev }: Props) {
  const [generating, setGenerating] = useState(false)
  const [generated, setGenerated] = useState(false)

  const handleGenerate = () => {
    setGenerating(true)
    // 模拟生成过程
    setTimeout(() => {
      setGenerating(false)
      setGenerated(true)
    }, 2000)
  }

  const generatePlan = () => {
    const { positioning, business, operation } = formData
    
    // 定位部分
    const locationTypeMap: Record<string, string> = {
      watertown: '江南水乡',
      mountain: '山水生态',
      cultural: '文化古迹',
      coastal: '滨海度假',
      rural: '田园乡村',
      urban: '城市更新',
    }

    const positioningMap: Record<string, string> = {
      ip: '文化IP型',
      ecology: '生态康养型',
      community: '社群运营型',
      immersive: '沉浸体验型',
      rural: '田园综合型',
      night: '夜间经济型',
    }

    // 业态部分
    const attractionMap: Record<string, string> = {
      landmark: '地标景观',
      performance: '演艺活动',
      experience: '沉浸体验',
      museum: '文化场馆',
      nature: '自然景观',
      night: '夜间项目',
    }

    const circulationMap: Record<string, string> = {
      loop: '环线式',
      spine: '主轴式',
      cluster: '组团式',
      network: '网络式',
    }

    // 运营部分
    const seasonMap: Record<string, string> = {
      spring: '春季（踏青赏花）',
      summer: '夏季（避暑亲水）',
      autumn: '秋季（丰收文化）',
      winter: '冬季（温泉暖冬）',
    }

    return {
      title: `${positioning.projectName || '文旅项目'} 策划方案`,
      summary: `本项目位于${positioning.location || '待定'}，依托${locationTypeMap[positioning.locationType] || '地域'}资源，以"${positioning.coreTheme || '文化'}"为核心主题，打造${positioningMap[positioning.positioning] || '特色'}文旅目的地。`,
      positioning: {
        location: positioning.location,
        locationType: locationTypeMap[positioning.locationType],
        targetGroup: positioning.targetGroup?.map((g: string) => g).join('、'),
        positioning: positioningMap[positioning.positioning],
        theme: positioning.coreTheme,
        competitors: positioning.competitors,
      },
      business: {
        attractions: business.coreAttraction?.map((a: string) => attractionMap[a]).filter(Boolean).join('、'),
        ratio: business.businessRatio,
        circulation: circulationMap[business.circulation],
        metrics: {
          stayDuration: business.stayDuration,
          ticketPrice: business.ticketPrice,
          capacity: business.annualCapacity,
        }
      },
      operation: {
        seasons: operation.seasonFocus?.map((s: string) => seasonMap[s]).filter(Boolean).join('、'),
        channels: operation.marketingChannels?.join('、'),
        community: operation.communityFeatures?.join('、'),
        ip: operation.ipCollaboration,
        differentiation: operation.differentiation,
      }
    }
  }

  const plan = generatePlan()

  const handleExport = (format: 'markdown' | 'text') => {
    const content = format === 'markdown' 
      ? generateMarkdown(plan)
      : generateText(plan)
    
    const blob = new Blob([content], { type: 'text/plain' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = `${plan.title}.${format === 'markdown' ? 'md' : 'txt'}`
    a.click()
    URL.revokeObjectURL(url)
  }

  const generateMarkdown = (plan: any) => `# ${plan.title}

## 项目概述

${plan.summary}

---

## 一、项目定位

### 1.1 地理位置
- **项目位置**: ${plan.positioning.location || '待定'}
- **资源类型**: ${plan.positioning.locationType || '待定'}

### 1.2 目标客群
${plan.positioning.targetGroup || '待定'}

### 1.3 项目定位
- **定位类型**: ${plan.positioning.positioning || '待定'}
- **核心主题**: ${plan.positioning.theme || '待定'}

### 1.4 竞品分析
${plan.positioning.competitors || '待定'}

---

## 二、业态规划

### 2.1 核心吸引物
${plan.business.attractions || '待定'}

### 2.2 业态配比
- 餐饮: ${plan.business.ratio?.catering || 30}%
- 零售: ${plan.business.ratio?.retail || 25}%
- 住宿: ${plan.business.ratio?.accommodation || 20}%
- 娱乐: ${plan.business.ratio?.entertainment || 15}%
- 服务: ${plan.business.ratio?.service || 10}%

### 2.3 动线设计
${plan.business.circulation || '待定'}

### 2.4 运营指标
- 停留时长: ${plan.business.metrics.stayDuration || '待定'}
- 门票价格: ${plan.business.metrics.ticketPrice || '待定'}
- 年容量: ${plan.business.metrics.capacity || '待定'}万人次

---

## 三、运营策略

### 3.1 四季运营
重点发力: ${plan.operation.seasons || '全年'}

### 3.2 营销渠道
${plan.operation.channels || '待定'}

### 3.3 社群运营
${plan.operation.community || '待定'}

### 3.4 IP 合作
${plan.operation.ip || '待定'}

### 3.5 差异化优势
${plan.operation.differentiation || '待定'}

---

*本方案由文旅策划生成器自动生成*
`

  const generateText = (plan: any) => `${plan.title}

项目概述：${plan.summary}

一、项目定位
地理位置：${plan.positioning.location || '待定'}
资源类型：${plan.positioning.locationType || '待定'}
目标客群：${plan.positioning.targetGroup || '待定'}
项目定位：${plan.positioning.positioning || '待定'}
核心主题：${plan.positioning.theme || '待定'}

二、业态规划
核心吸引物：${plan.business.attractions || '待定'}
业态配比：餐饮${plan.business.ratio?.catering || 30}% / 零售${plan.business.ratio?.retail || 25}% / 住宿${plan.business.ratio?.accommodation || 20}% / 娱乐${plan.business.ratio?.entertainment || 15}% / 服务${plan.business.ratio?.service || 10}%
动线设计：${plan.business.circulation || '待定'}

三、运营策略
四季运营：${plan.operation.seasons || '全年'}
营销渠道：${plan.operation.channels || '待定'}
社群运营：${plan.operation.community || '待定'}

本方案由文旅策划生成器自动生成
`

  if (!generated) {
    return (
      <div className="bg-white rounded-2xl shadow-lg p-8">
        <div className="text-center py-12">
          <div className="text-6xl mb-6">📄</div>
          <h2 className="text-2xl font-bold text-gray-800 mb-4">生成策划方案</h2>
          <p className="text-gray-600 mb-8 max-w-md mx-auto">
            基于你填写的项目定位、业态规划和运营策略，AI 将生成一份完整的文旅策划方案
          </p>

          {generating ? (
            <div className="flex flex-col items-center">
              <div className="w-12 h-12 border-4 border-orange-200 border-t-orange-500 rounded-full animate-spin mb-4"></div>
              <p className="text-gray-600">正在生成策划方案...⏳</p>
            </div>
          ) : (
            <button
              onClick={handleGenerate}
              className="px-8 py-4 bg-gradient-to-r from-orange-500 to-amber-600 text-white font-bold rounded-lg hover:shadow-lg transition-all text-lg"
            >
              ✨ 一键生成方案
            </button>
          )}
        </div>

        <div className="mt-8 flex justify-start">
          <button
            onClick={onPrev}
            className="px-6 py-3 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-all"
          >
            ← 返回修改
          </button>
        </div>
      </div>
    )
  }

  return (
    <div className="bg-white rounded-2xl shadow-lg p-8">
      <div className="mb-6 flex items-center justify-between">
        <div>
          <h2 className="text-2xl font-bold text-gray-800">📄 {plan.title}</h2>
          <p className="text-gray-600 mt-1">策划方案已生成</p>
        </div>
        <div className="flex gap-2">
          <button
            onClick={() => handleExport('markdown')}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
          >
            导出 Markdown
          </button>
          <button
            onClick={() => handleExport('text')}
            className="px-4 py-2 bg-gray-100 text-gray-700 rounded-lg hover:bg-gray-200 transition-all"
          >
            导出文本
          </button>
        </div>
      </div>

      <div className="prose max-w-none">
        {/* 项目概述 */}
        <div className="bg-orange-50 p-6 rounded-xl mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-3">📝 项目概述</h3>
          <p className="text-gray-700">{plan.summary}</p>
        </div>

        {/* 项目定位 */}
        <div className="mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-4 border-b pb-2">一、项目定位</h3>
          
          <div className="grid grid-cols-2 gap-4">
            <div className="bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500">地理位置</div>
              <div className="font-medium text-gray-800">{plan.positioning.location || '待定'}</div>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500">资源类型</div>
              <div className="font-medium text-gray-800">{plan.positioning.locationType || '待定'}</div>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500">目标客群</div>
              <div className="font-medium text-gray-800">{plan.positioning.targetGroup || '待定'}</div>
            </div>
            <div className="bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500">项目定位</div>
              <div className="font-medium text-gray-800">{plan.positioning.positioning || '待定'}</div>
            </div>
          </div>

          <div className="mt-4 bg-gray-50 p-4 rounded-lg">
            <div className="text-sm text-gray-500 mb-1">核心文化主题</div>
            <div className="font-medium text-gray-800">{plan.positioning.theme || '待定'}</div>
          </div>

          {plan.positioning.competitors && (
            <div className="mt-4 bg-gray-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500 mb-1">竞品分析</div>
              <div className="font-medium text-gray-800">{plan.positioning.competitors}</div>
            </div>
          )}
        </div>

        {/* 业态规划 */}
        <div className="mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-4 border-b pb-2">二、业态规划</h3>
          
          {plan.business.attractions && (
            <div className="mb-4">
              <div className="text-sm text-gray-500 mb-2">核心吸引物</div>
              <div className="flex flex-wrap gap-2">
                {plan.business.attractions.split('、').map((attr: string) => (
                  <span key={attr} className="px-3 py-1 bg-orange-100 text-orange-700 rounded-full text-sm">
                    {attr}
                  </span>
                ))}
              </div>
            </div>
          )}

          <div className="mb-4">
            <div className="text-sm text-gray-500 mb-2">业态配比</div>
            <div className="space-y-2">
              {plan.business.ratio && Object.entries(plan.business.ratio).map(([key, value]: [string, any]) => {
                const labels: Record<string, string> = {
                  catering: '餐饮',
                  retail: '零售',
                  accommodation: '住宿',
                  entertainment: '娱乐',
                  service: '服务'
                }
                return (
                  <div key={key} className="flex items-center gap-3">
                    <div className="w-16 text-sm text-gray-600">{labels[key]}</div>
                    <div className="flex-1 bg-gray-200 rounded-full h-4 overflow-hidden">
                      <div 
                        className="bg-gradient-to-r from-orange-400 to-amber-500 h-full rounded-full"
                        style={{ width: `${value}%` }}
                      />
                    </div>
                    <div className="w-12 text-right text-sm font-medium text-gray-700">{value}%</div>
                  </div>
                )
              })}
            </div>
          </div>

          <div className="grid grid-cols-3 gap-3">
            <div className="bg-gray-50 p-3 rounded-lg">
              <div className="text-xs text-gray-500">动线设计</div>
              <div className="font-medium text-gray-800">{plan.business.circulation || '待定'}</div>
            </div>
            <div className="bg-gray-50 p-3 rounded-lg">
              <div className="text-xs text-gray-500">停留时长</div>
              <div className="font-medium text-gray-800">{plan.business.metrics.stayDuration || '待定'}</div>
            </div>
            <div className="bg-gray-50 p-3 rounded-lg">
              <div className="text-xs text-gray-500">门票价格</div>
              <div className="font-medium text-gray-800">{plan.business.metrics.ticketPrice || '待定'}</div>
            </div>
          </div>
        </div>

        {/* 运营策略 */}
        <div className="mb-6">
          <h3 className="text-lg font-bold text-gray-800 mb-4 border-b pb-2">三、运营策略</h3>
          
          {plan.operation.seasons && (
            <div className="mb-4">
              <div className="text-sm text-gray-500 mb-2">四季运营重点</div>
              <div className="flex flex-wrap gap-2">
                {plan.operation.seasons.split('、').map((season: string) => (
                  <span key={season} className="px-3 py-1 bg-green-100 text-green-700 rounded-full text-sm">
                    {season}
                  </span>
                ))}
              </div>
            </div>
          )}

          {plan.operation.channels && (
            <div className="mb-4">
              <div className="text-sm text-gray-500 mb-2">营销渠道</div>
              <div className="flex flex-wrap gap-2">
                {plan.operation.channels.split('、').map((channel: string) => (
                  <span key={channel} className="px-3 py-1 bg-blue-100 text-blue-700 rounded-full text-sm">
                    {channel}
                  </span>
                ))}
              </div>
            </div>
          )}

          {plan.operation.differentiation && (
            <div className="bg-gradient-to-r from-orange-50 to-amber-50 p-4 rounded-lg">
              <div className="text-sm text-gray-500 mb-1">差异化优势</div>
              <div className="font-medium text-gray-800">{plan.operation.differentiation}</div>
            </div>
          )}
        </div>
      </div>

      <div className="mt-8 flex justify-between">
        <button
          onClick={onPrev}
          className="px-6 py-3 border border-gray-300 text-gray-700 font-medium rounded-lg hover:bg-gray-50 transition-all"
        >
          ← 返回修改
        </button>
        <button
          onClick={() => {
            setGenerated(false)
            setGenerating(false)
          }}
          className="px-6 py-3 bg-orange-100 text-orange-700 font-medium rounded-lg hover:bg-orange-200 transition-all"
        >
          🔄 重新生成
        </button>
      </div>
    </div>
  )
}
