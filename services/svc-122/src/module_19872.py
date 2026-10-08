"""Service module 19872: business logic, no crypto."""


def calculate_total_19872(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_19872():
    return 'module 19872 handles orders and invoices'
