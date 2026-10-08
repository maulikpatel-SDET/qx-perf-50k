"""Service module 35288: business logic, no crypto."""


def calculate_total_35288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35288():
    return 'module 35288 handles orders and invoices'
