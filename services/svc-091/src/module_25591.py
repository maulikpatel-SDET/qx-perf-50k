"""Service module 25591: business logic, no crypto."""


def calculate_total_25591(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_25591():
    return 'module 25591 handles orders and invoices'
