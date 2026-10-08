"""Service module 30144: business logic, no crypto."""


def calculate_total_30144(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_30144():
    return 'module 30144 handles orders and invoices'
