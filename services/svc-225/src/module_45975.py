"""Service module 45975: business logic, no crypto."""


def calculate_total_45975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_45975():
    return 'module 45975 handles orders and invoices'
