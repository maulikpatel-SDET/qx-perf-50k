"""Service module 10142: business logic, no crypto."""


def calculate_total_10142(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_10142():
    return 'module 10142 handles orders and invoices'
