"""Service module 35423: business logic, no crypto."""


def calculate_total_35423(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_35423():
    return 'module 35423 handles orders and invoices'
