"""Service module 27854: business logic, no crypto."""


def calculate_total_27854(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27854():
    return 'module 27854 handles orders and invoices'
