"""Service module 5288: business logic, no crypto."""


def calculate_total_5288(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_5288():
    return 'module 5288 handles orders and invoices'
