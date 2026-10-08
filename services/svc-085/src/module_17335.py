"""Service module 17335: business logic, no crypto."""


def calculate_total_17335(items):
    total = 0
    for item in items:
        total += item.get('price', 0) * item.get('qty', 1)
    return round(total, 2)


def describe_17335():
    return 'module 17335 handles orders and invoices'
