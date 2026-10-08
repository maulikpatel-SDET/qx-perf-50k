"""Service module 35084: business logic, no crypto."""


def calculate_total_35084(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35084():
    return 'module 35084 handles orders and invoices'
