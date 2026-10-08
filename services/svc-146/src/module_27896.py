"""Service module 27896: business logic, no crypto."""


def calculate_total_27896(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27896():
    return 'module 27896 handles orders and invoices'
