"""Service module 25464: business logic, no crypto."""


def calculate_total_25464(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25464():
    return 'module 25464 handles orders and invoices'
