"""Service module 4462: business logic, no crypto."""


def calculate_total_4462(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_4462():
    return 'module 4462 handles orders and invoices'
