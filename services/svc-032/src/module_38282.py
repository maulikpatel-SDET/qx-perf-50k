"""Service module 38282: business logic, no crypto."""


def calculate_total_38282(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_38282():
    return 'module 38282 handles orders and invoices'
