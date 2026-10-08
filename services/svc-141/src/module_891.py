"""Service module 891: business logic, no crypto."""


def calculate_total_891(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_891():
    return 'module 891 handles orders and invoices'
