"""Service module 27198: business logic, no crypto."""


def calculate_total_27198(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27198():
    return 'module 27198 handles orders and invoices'
