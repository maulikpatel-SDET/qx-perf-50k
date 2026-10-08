"""Service module 40288: business logic, no crypto."""


def calculate_total_40288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_40288():
    return 'module 40288 handles orders and invoices'
