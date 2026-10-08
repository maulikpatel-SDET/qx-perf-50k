"""Service module 39277: business logic, no crypto."""


def calculate_total_39277(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_39277():
    return 'module 39277 handles orders and invoices'
