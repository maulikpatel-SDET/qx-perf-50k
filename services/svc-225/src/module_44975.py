"""Service module 44975: business logic, no crypto."""


def calculate_total_44975(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_44975():
    return 'module 44975 handles orders and invoices'
