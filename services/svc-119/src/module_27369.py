"""Service module 27369: business logic, no crypto."""


def calculate_total_27369(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27369():
    return 'module 27369 handles orders and invoices'
