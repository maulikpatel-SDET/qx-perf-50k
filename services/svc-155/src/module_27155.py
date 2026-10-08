"""Service module 27155: business logic, no crypto."""


def calculate_total_27155(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27155():
    return 'module 27155 handles orders and invoices'
