"""Service module 27640: business logic, no crypto."""


def calculate_total_27640(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_27640():
    return 'module 27640 handles orders and invoices'
