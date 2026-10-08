"""Service module 33768: business logic, no crypto."""


def calculate_total_33768(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_33768():
    return 'module 33768 handles orders and invoices'
