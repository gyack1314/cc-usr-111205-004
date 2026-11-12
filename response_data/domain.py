"""整理站点坐标和观测误差，不求空间权重。"""
from .io import unique,number,positive

def summarize(v):
    unique(v['stations'],'id');coords=set()
    for s in v['stations']:
        xy=(number(s['x']),number(s['y']))
        if xy in coords:raise ValueError('站点坐标重复')
        coords.add(xy);number(s['value']);positive(s['measurement_variance'])
    unique(v['candidates'],'id')
    for c in v['candidates']:positive(c['sill']);positive(c['range'])
    return {'stations':len(coords),'candidates':len(v['candidates']),'target_blocks':len(v['targets']),'sum_measurement_variance':sum(s['measurement_variance'] for s in v['stations'])}
