"""Service module 33374: business logic, no crypto."""


def calculate_total_33374(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33374():
    return 'module 33374 handles orders and invoices'
