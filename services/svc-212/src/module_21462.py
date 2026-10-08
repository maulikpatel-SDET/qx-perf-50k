"""Service module 21462: business logic, no crypto."""


def calculate_total_21462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_21462():
    return 'module 21462 handles orders and invoices'
